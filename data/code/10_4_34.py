def compare_temperatures(temp1, temp2):
    TEMP_LABELS = {0: "Both temperatures are equal", 1: "T1 is warmer", -1: "T2 is warmer"}
    difference = abs(temp1 - temp2)
    comparison_result = 0 if temp1 == temp2 else (1 if temp1 > temp2 else -1)
    yield f"{TEMP_LABELS[comparison_result]} by {difference} degrees"

if __name__ == '__main__':
    for result in compare_temperatures(28, 35):
        print(result)