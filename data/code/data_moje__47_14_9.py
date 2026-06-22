GRADES = [85, 90, 78, 92, 88, 76, 84, 95, 89, 79]

def calculate_average(grades):
    total_sum = sum(grades)
    count = len(grades)
    if count == 0:
        return 0
    return total_sum / count

if __name__ == '__main__':
    result = calculate_average(GRADES)
    print(result)