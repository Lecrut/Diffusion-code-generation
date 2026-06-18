def compare_temperatures(temp1: float, temp2: float) -> None:
    """Yields a string describing the comparison result between two temperatures."""
    difference = abs(temp1 - temp2)
    
    if temp1 > temp2:
        yield f"{temp1} is warmer by {difference:.1f} degrees than {temp2}"
    elif temp2 > temp1:
        yield f"{temp2} is warmer by {difference:.1f} degrees than {temp1}"
    else:
        yield "Both temperatures are equal"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    temp_a = 75.0
    temp_b = 68.3
    
    print("Comparison Results:")
    results = compare_temperatures(temp_a, temp_b)
    
    for result in results:
        print(result)

# Additional test case commented out to ensure single runnable module structure without extra inputs
# if __name__ == '__main__':
#     temp_c = -10.5
#     temp_d = 2.7
#     
#     print("\nSecond Test Case:")
#     for result in compare_temperatures(temp_c, temp_d):
#         print(result)