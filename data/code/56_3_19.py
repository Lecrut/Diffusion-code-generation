def generate_seven_times_table():
    return [f"{i} x 7 = {i * 7}" for i in range(1, 11)]

if __name__ == '__main__':
    result = generate_seven_times_table()
    for line in result:
        print(line)