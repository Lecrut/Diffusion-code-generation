def compare_temperatures(temp1, temp2):
    diff = abs(temp1 - temp2)
    if temp1 > temp2:
        yield f"T1 is warmer by {diff} degrees"
    elif temp2 > temp1:
        yield f"T2 is warmer by {diff} degrees"
    else:
        yield "Both temperatures are equal"

if __name__ == '__main__':
    for result in compare_temperatures(75, 68):
        print(result)