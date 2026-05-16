if __name__ == '__main__':
    input_string = "10,20,30,40,50"
    numbers = input_string.split(',')
    float_list = [float(num.strip()) for num in numbers]
    if float_list:
        average = sum(float_list) / len(float_list)
        print(average)
    else:
        print("No numbers found")