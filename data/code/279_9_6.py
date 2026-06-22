if __name__ == '__main__':
    start_num = 1
    end_num = 100

    def is_divisible_by_3_and_5(num):
        return num % 3 == 0 and num % 5 == 0

    for i in range(start_num, end_num + 1):
        if is_divisible_by_3_and_5(i):
            print(i)