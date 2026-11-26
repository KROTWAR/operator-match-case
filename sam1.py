month = int(input("Введите номер месяца"))
match month:
    case 12 | 1 | 2:
        print(f"Это зима")
    case 3 | 4 | 5:
        print(f"Это весна")
    case 6 | 7 | 8:
        print(f"Это лето")
    case 9 | 10 | 11:
        print(f"Это осень")
    case _:
        print("ошибка")