calculate_average = lambda numbers: sum(numbers) / len(numbers)

if __name__ == '__main__':
    values = [2.0, 4.5, 6.0, 8.5]
    avg = calculate_average(values)
    print(avg)