def compare_temperatures(temp1, temp2):
    DIFFERENCE_MESSAGES = {
        0: "Both temperatures are equal",
        1: lambda diff: f"T1 is warmer by {diff} degrees",
        -1: lambda diff: f"T2 is warmer by {diff} degrees"
    }
    
    difference = abs(temp1 - temp2)
    comparison_result = 0 if temp1 == temp2 else (1 if temp1 > temp2 else -1)
    
    yield DIFFERENCE_MESSAGES[comparison_result](difference)

if __name__ == '__main__':
    for result in compare_temperatures(30, 25):
        print(result)
    for result in compare_temperatures(28, 35):
        print(result)
    for result in compare_temperatures(20, 20):
        print(result)
    for result in compare_temperatures(15, 22):
        print(result)