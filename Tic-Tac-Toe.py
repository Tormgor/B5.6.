# Функции программы
# Функция aормирования игрового поля.
def playing_field():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

# Функция интерфейса ввода.
def interface():
    while True:
        cords = input("     Координаты вашего хода: ").split()

        if len(cords) != 2:
            print(" Введите две цифры! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите цифры! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Введите цифры от 0 до 2 . ")
            continue

        if field[x][y] != " ":
            print(" В эту ячейку уже был сделан ход. ")
            continue

        return x, y

# Функция проверки.
def checks():
    matrix_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in matrix_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print(" Выйграл первый игрок. Поздравляем!")
            return True
        if symbols == ["0", "0", "0"]:
            print(" Выйграл второй игрок. Поздравляем!")
            return True
    return False

# Основная программа.
print(" Игра Крестики Нолики !")
print("                       ")
print(" Правила игры: ")
print(" Играют два игрока, которые ходят по очереди. ")
print(" Первый  игрок 'ходит' крестиком, а второй ноликом. ")
print(" Положение своего хода, указывают номером ячейки.")
print(" Первая цифра по вертикали, вторая по горизонтали, ")
print(" двумя цифрами, через пробел.")

field = [[" "] * 3 for i in range(3)]# Поле 3х3
count = 0
while True:
    count += 1
    playing_field()
    if count % 2 == 1:
        print(" Ход первого игрока:")
    else:
        print(" Ход второго игрока:")

    x, y = interface()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if checks():
        break
        
    if count == 9:
        print(" Ничья.")
        break
