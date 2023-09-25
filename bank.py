from keyboard import is_pressed
import matplotlib.pyplot as plt


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i+1, y[i], y[i], ha='center')


def bank():
    s = int(input('Enter sum: '))
    perc = float(input('Percent: ')) / 100
    period = float(input("How many years: "))
    print('\n')
    a = s
    m = 1
    mList = []
    sumList = []
    mList1 = []
    sumList1 = []
    profitList = []
    for i in range(int(12 * period)):
        s = round(s * perc / 12 + s, 2)
        b = round(s * perc / 12, 2)
        print(f'{m} month: {s} rub.\n profit: {int(s - a)} rub., (+ {b} rub.)\n')

        r = str(int(s)) + ' +' + str(int(b))
        mList.append(str(m) + ' month')
        sumList.append(r)
        profitList.append(int(b))

        mList1.append(int(m))
        sumList1.append(int(s))

        m = m + 1

    d = dict(map(lambda k, v: (k, v), mList, sumList))
    '''for keys, values in d.items():
        print(f'{keys}: {values}\n')'''
    with open('bank', 'w+') as f:
        for keys, values in d.items():
            f.write(f'{keys}, {values}\n')

    d1 = dict(map(lambda k, v: (k, v), mList1, sumList1))
    x = list(d1.keys())
    y = list(d1.values())
    plt.figure(figsize=(10, 5))
    plt.bar(x, y, color='pink')
    addlabels(x, y)
    plt.xlabel('Months')
    plt.ylabel('Money')
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(mList1, profitList, color='yellow')
    addlabels(mList1, profitList)
    plt.xlabel('Months')
    plt.ylabel('profit')
    plt.show()


while True:
    try:
        print('Enter \'s\' to start and \'e\' to exit: ')
        while True:
            if is_pressed('s'):
                print(' ')
                print('*****START***** ')
                bank()
                break
            elif is_pressed('e'):
                print(' ')
                print('EXIT...')
                break
        if is_pressed('e'):
            break
    except BaseException as e:
        print(e, '\n****PLEASE TRY AGAIN!****')
        print(' ')
