from operator import itemgetter
weekdays = {1: 'MN.txt', 2: 'TUE.txt', 3: 'WDN.txt', 4: 'THU.txt', 5: 'FR.txt', 6: "STD.txt", 7: 'SUN.txt'}
schedule_change = int(input('Введите 1 для чтения, 2 - для добавления, 3 - для замены: '))
while schedule_change < 1 or schedule_change > 3:
    schedule_change = int(input('Ошибка. Попробуйте еще раз ( Выберите 1, 2 или 3) : '))

if schedule_change == 1:
    day = int(input('Введите день недели (от 1 до 7): '))
    with open(weekdays[day], 'r', encoding='utf-8') as my_f:
        while True:
            line = my_f.readline()
            if not line:
                break
            print(line.strip())
elif schedule_change == 2:
    day = int(input('Введите день недели (от 1 до 7): '))
    event_count = int(input('Введите количество мероприятий: '))
    with open(weekdays[day], 'a', encoding='utf-8') as my_f:
            while True:
                dict_time = {}
                sorted(dict_time.keys())
                for num in range(event_count):
                    event = input('Какое мероприятие вы желаете добавить? ')
                    time_it = str(input('На какое время:  '))
                    dict_time[time_it] = event
                    my_f.write(str(time_it))
                    my_f.write('\n')
                    my_f.write(event)
                    my_f.write('\n')
                break



elif schedule_change == 3:
    day = int(input('Введите день недели (от 1 до 7): '))
    event = input('Какое мероприятие вы желаете добавить? ')
    time_it = str(input('На какое время:  '))
    with open(weekdays[day], 'w', encoding='utf-8') as my_f:
        my_f.write(time_it)
        my_f.write('\n')
        my_f.write(event)