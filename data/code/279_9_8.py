if __name__ == '__main__':
    start_num = 1
    end_num = 100
    if not (isinstance(start_num, int) and isinstance(end_num, int)):
        raise ValueError("Both start_num and end_num must be integers")
    
    for i in range(start_num, end_num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)