def main():
    condition1 = True
    condition2 = False
    condition3 = True
    print("--- Test Case 1: True or False ---")
    result1 = condition1 or condition2
    print(f"Condition 1: {condition1}, Condition 2: {condition2}")
    print(f"Result (True or False): {result1}")
    print("\n--- Test Case 2: True or True ---")
    result2 = condition1 or condition3
    print(f"Condition 1: {condition1}, Condition 3: {condition3}")
    print(f"Result (True or True): {result2}")
    print("\n--- Test Case 3: False or False ---")
    condition4 = False
    condition5 = False
    result3 = condition4 or condition5
    print(f"Condition 4: {condition4}, Condition 5: {condition5}")
    print(f"Result (False or False): {result3}")
    print("\n--- Test Case 4: False or True ---")
    condition6 = False
    condition7 = True
    result4 = condition6 or condition7
    print(f"Condition 6: {condition6}, Condition 7: {condition7}")
    print(f"Result (False or True): {result4}")
if __name__ == '__main__':
    main()