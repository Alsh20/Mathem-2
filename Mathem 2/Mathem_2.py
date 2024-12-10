rules = {
    1: {  # sin
        "0 -": "-sin(alpha)", "0 +": "sin(alpha)",
        "90 -": "cos(alpha)", "90 +": "cos(alpha)", "pi/2 -": "cos(alpha)", "pi/2 +": "cos(alpha)",
        "180 -": "sin(alpha)", "180 +": "-sin(alpha)", "pi -": "sin(alpha)", "pi +": "-sin(alpha)",
        "270 -": "-cos(alpha)", "270 +": "-cos(alpha)", "3pi/2 -": "-cos(alpha)", "3pi/2 +": "-cos(alpha)",
        "360 -": "-sin(alpha)", "360 +": "sin(alpha)", "2pi -": "-sin(alpha)", "2pi +": "sin(alpha)"
    },
    2: {  # cos
        "0 -": "cos(alpha)", "0 +": "cos(alpha)",
        "90 -": "sin(alpha)", "90 +": "-sin(alpha)", "pi/2 -": "sin(alpha)", "pi/2 +": "-sin(alpha)",
        "180 -": "-cos(alpha)", "180 +": "-cos(alpha)", "pi -": "-cos(alpha)", "pi +": "-cos(alpha)",
        "270 -": "-sin(alpha)", "270 +": "sin(alpha)", "3pi/2 -": "-sin(alpha)", "3pi/2 +": "sin(alpha)",
        "360 -": "cos(alpha)", "360 +": "cos(alpha)", "2pi -": "cos(alpha)", "2pi +": "cos(alpha)"
    },
    3: {  # tg
        "0 -": "-tg(alpha)", "0 +": "tg(alpha)",
        "90 -": "ctg(alpha)", "90 +": "-ctg(alpha)", "pi/2 -": "ctg(alpha)", "pi/2 +": "-ctg(alpha)",
        "180 -": "-tg(alpha)", "180 +": "tg(alpha)", "pi -": "-tg(alpha)", "pi +": "tg(alpha)",
        "270 -": "ctg(alpha)", "270 +": "-ctg(alpha)", "3pi/2 -": "ctg(alpha)", "3pi/2 +": "-ctg(alpha)",
        "360 -": "-tg(alpha)", "360 +": "tg(alpha)", "2pi -": "-tg(alpha)", "2pi +": "tg(alpha)"
    },
    4: {  # ctg
        "0 -": "-ctg(alpha)", "0 +": "ctg(alpha)",
        "90 -": "tg(alpha)", "90 +": "-tg(alpha)", "pi/2 -": "tg(alpha)", "pi/2 +": "-tg(alpha)",
        "180 -": "-ctg(alpha)", "180 +": "ctg(alpha)", "pi -": "-ctg(alpha)", "pi +": "ctg(alpha)",
        "270 -": "tg(alpha)", "270 +": "-tg(alpha)", "3pi/2 -": "tg(alpha)", "3pi/2 +": "-tg(alpha)",
        "360 -": "-ctg(alpha)", "360 +": "ctg(alpha)", "2pi -": "-ctg(alpha)", "2pi +": "ctg(alpha)"
    }
}

while True:
    x = input("Выберите 1) sin(alpha), 2) cos(alpha), 3) tg(alpha), 4) ctg(alpha) или 'exit' для выхода: ")
    if x.lower() == 'exit':
        print("Программа завершена.")
        break
    
    try:
        x = int(x)
        if x not in rules:
            print("Выберите число от 1 до 4.")
            continue
        
        f = input("Напишите градус или радиан (+ или -) alpha: ").strip()
        if f in rules[x]:
            print(f"Жауабы: {rules[x][f]}")
        else:
            print("Неправильный синтаксис. Проверьте ввод.")
    except ValueError:
        print("Введите корректное число от 1 до 4 или 'exit' для выхода.")

