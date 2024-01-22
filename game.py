import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0  # Счетчик
    limits = (1, 100)  # Стартоаые лимиты
    for i in range(0, 20):
        count += 1
        predict = int(abs(limits[1] - limits[0]) / 2) + limits[0]  # Лимит половиним и прибавляем нижнюю границу
        if predict > number:
            limits = (limits[0], limits[1] - int(abs(limits[1] - limits[0]) / 2))  # Если искомое меньше
        elif predict < number:
            limits = (limits[0] + int(abs(limits[1] - limits[0]) / 2), limits[1])  # Если искомое больше
        else:
            break
    # Ваш код заканчивается здесь

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


if __name__ == '__main__':
    score_game(game_core_v3)
