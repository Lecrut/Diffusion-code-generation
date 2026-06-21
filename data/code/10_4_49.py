def compare_temperatures(temp1, temp2):
    def format_result(label, difference):
        return f"{label} by {difference} degrees"

    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        yield format_result("T1 is warmer", difference)
    elif temp2 > temp1:
        yield format_result("T2 is warmer", difference)
    else:
        yield "Both temperatures are equal"

if __name__ == '__main__':
    for result in compare_temperatures(20, 18):
        print(result)
    for result in compare_temperatures(25, 30):
        print(result)
    for result in compare_temperatures(27, 27):
        print(result)