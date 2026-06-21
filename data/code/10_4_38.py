TEMPERATURE_EQUAL = 0
TEMPERATURE_T1_WARMER = 1
TEMPERATURE_T2_WARMER = -1

def compare_temperatures(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Temperature must be a number")
    
    difference = abs(temp1 - temp2)
    comparison_result = TEMPERATURE_EQUAL if temp1 == temp2 else (TEMPERATURE_T1_WARMER if temp1 > temp2 else TEMPERATURE_T2_WARMER)
    
    if comparison_result == TEMPERATURE_EQUAL:
        yield "Both temperatures are equal"
    elif comparison_result == TEMPERATURE_T1_WARMER:
        yield f"T1 is warmer by {difference} degrees"
    else:
        yield f"T2 is warmer by {difference} degrees"

if __name__ == '__main__':
    sample_values = [(30, 25), (28, 35), (20, 20), (15, 22)]
    for temp1, temp2 in sample_values:
        for result in compare_temperatures(temp1, temp2):
            print(result)