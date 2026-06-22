if __name__ == '__main__':
    start_num = 1
    end_num = 100
    for i in range(start_num, end_num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)