import random


def main():
    total = 0
    numbers = []
    i = 0

    while total < 100:
        numbers.append(random.randint(0, 100))
        total += numbers[i]
        if total > 100:
            total -= numbers[i]
            break
        i += 1

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
