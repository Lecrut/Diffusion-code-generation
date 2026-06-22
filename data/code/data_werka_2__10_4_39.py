def compare_temperatures(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Temperatures must be numbers")
    
    difference = abs(temp1 - temp2)
    warmer_label = "T1" if temp1 > temp2 else "T2"
    
    if temp1 == temp2:
        yield "Both temperatures are equal"
    else:
        yield f"{warmer_label} is warmer by {difference} degrees"

if __name__ == '__main__':
    for result in compare_temperatures(40, 38):
        print(result)