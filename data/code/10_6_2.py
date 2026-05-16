def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        difference = temp1 - temp2
        yield f"Temperature 1 is warmer by {difference} degrees"
    elif temp2 > temp1:
        difference = temp2 - temp1
        yield f"Temperature 2 is warmer by {difference} degrees"
    else:
        yield "Temperatures are equal"
if __name__ == '__main__':
    for t1, t2 in [(30, 25), (15, 15), (40, 35), (5, 10)]:
        for result in compare_temperatures(t1, t2):
            print(result)