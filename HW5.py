def move_last_to_first(lst):
    # Проверка, пустой ли список или есть только один элемент
    if len(lst) <= 1:
        return lst
    # Берем последний элемент и добавляем его на начало списка

    return  [lst[-1]] + lst[1:-1] + [lst[0]]
# Приклади для перевірки
print(move_last_to_first([12, 3, 4, 10]))  # [10, 3, 4, 12]
print(move_last_to_first([1]))            # [1]
print(move_last_to_first([]))             # []
print(move_last_to_first([12, 3, 4, 10, 8]))  # [8,3,4,10,12]