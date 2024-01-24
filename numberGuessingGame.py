from random import randint

MAX_GUESSES = 10
MIN_NUM = 1
MAX_NUM = 10

def main():
    print('Добро пожаловать в игру "Угадай число"!')
    MIN_NUM = input("Введите диапазон чисел\nОт:")
    while not MIN_NUM.isdecimal(): print(f"Надо написать число!"); MIN_NUM = input("Введите корекктное число\nОт:")
    MAX_NUM = input("До:")
    while not MAX_NUM.isdecimal() or not int(MAX_NUM) >= int(MIN_NUM): print(f"Надо написать число больше {MIN_NUM}!"); MAX_NUM = input("Введите корекктное число\nДо:")
    MIN_NUM = int(MIN_NUM)
    MAX_NUM = int(MAX_NUM)

    print(
        f"""
        В этой игре у вас всего {MAX_GUESSES} попыток угадать число в диапазоне от {MIN_NUM} до {MAX_NUM}
        Примечание: введите e, чтобы завершить игрy
        """
    )
    gameover = 0
    esc = 1

    while not gameover:
        secret_num = randint(MIN_NUM, MAX_NUM)
        print("Я загадал число.")
        print(f"У вас есть {MAX_GUESSES} попыток, чтобы угадать.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES and not gameover:
            guess = ""

            while not gameover:
                print(f"Попытка {num_guesses}")
                guess = input("> ")

                if guess == "esc":
                    gameover = 1
                    esc = 0
                    break

                if len(guess) not in range(MIN_NUM, MAX_NUM+1) or not guess.isdecimal():
                    print(f"Надо написать число От: {MIN_NUM} До: {MAX_NUM} или esc для выхода!")
                    continue
                guess = int(guess)

                answer = get_answer(guess, secret_num)
                print(answer)
                num_guesses += 1

                if guess == secret_num:
                    gameover = 1
                    break

                if num_guesses > MAX_GUESSES:
                    print("У вас закончились попытки.😞")
                    print(f"Правильный ответ: {secret_num}")
                    break
        
        if esc:
            print("Хотите сыграть еще раз? (1-да/2-нет)")
            inp = input("> ")
            while inp not in ("1", "2"):
                print("Напишите 1 или 2")
                inp = input("> ")
            if int(inp) == 1: main()
            elif int(inp) == 2: break; gameover = 1
    print("Спасибо за игру")


def get_answer(guess, secret_num):
    if guess == secret_num:
        return "Вы угадали!!!"

    elif guess < secret_num:
        return f"Число {guess} меньше чем загаданное"
    elif guess > secret_num:
        return f"Число {guess} больше чем загаданное"


if __name__ == "__main__":
    main()
