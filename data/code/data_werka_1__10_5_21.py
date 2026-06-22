def compare_temperatures(temp1, temp2, label1='T1', label2='T2'):
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        yield f"{label1} is warmer by {difference:.2f} degrees"
    elif temp2 > temp1:
        yield f"{label2} is warmer by {difference:.2f} degrees"
    else:
        yield "Both temperatures are equal"

if __name__ == '__main__':
    t1 = 75.5
    t2 = 68.3
    for result in compare_temperatures(t1, t2):
        print(result)