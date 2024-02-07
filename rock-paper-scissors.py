import random

# Перелік дій
ACTIONS: dict[int, str] = {0: "Rock", 1: "Paper", 2: "Scissors"}

# Перелік переможних варіантів, де ключ - переможець, а значення - програшник
VICTORIES: dict[str, str] = {
    "Rock": "Scissors",  # Камінь перемагає ножиці
    "Paper": "Rock",  # Папір перемагає камінь
    "Scissors": "Paper",  # Ножиці перемагають папір
}


def get_user_selection(actions: dict[int, str]) -> str:
    """Отримує вибір користувача та повертає дію у вигляді рядка."""
    choices: list[str] = [f"{actions[action]}[{action}]" for action in actions]
    choices_str: str = ", ".join(choices)
    selection: int = int(input(f"Enter a choice ({choices_str}): "))
    action: str = actions[selection]
    return action


def get_computer_selection(actions: dict[int, str]) -> str:
    """Генерує випадковий вибір комп'ютера та повертає дію у вигляді рядка."""
    selection: int = random.randint(0, len(actions) - 1)
    action: str = actions[selection]
    return action


def get_determine_winner(
    victories: dict[str, str], user_action: str, computer_action: str
) -> str:
    """Визначає переможця гри та повертає результат."""
    defeats: str = victories[user_action]
    if user_action == computer_action:
        result = f"Both players selected {user_action}. It's a tie!"
    elif computer_action in defeats:
        result = f"{user_action} beats {computer_action}! You win!"
    else:
        result = f"{computer_action} beats {user_action}! You lose."
    return result


if __name__ == "__main__":
    # Ігри йдуть вічно одна за одною
    while True:
        try:
            # Отримується вибір користувача
            user_selection: str = get_user_selection(ACTIONS)
            print(user_selection)
            # Отримується випадковий вибір комп'ютера
            computer_selection: str = get_computer_selection(ACTIONS)
            print(computer_selection)
            # Визначення переможця гри
            determine_winner: str = get_determine_winner(
                VICTORIES, user_selection, computer_selection
            )
            # Виводить результат гри
            print(determine_winner)
        # Якщо з'явилася помилка, або вибрано не те, що можна було
        except:
            range_str: str = f"[0, {len(ACTIONS) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            # Гра починається спочатку, адже обрав він неіснуючий варіант
            continue
        # Якщо гра пройшла успішно, запитуємо чи ще хоче гравець грати?
        play_again: str = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
