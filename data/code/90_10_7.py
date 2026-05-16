def main():
    condition1 = True
    condition2 = False
    condition3 = False
    print("--- Test Case 1: True or False ---")
    result1 = condition1 or condition2
    print(f"Condition 1: {condition1}, Condition 2: {condition2}")
    print(f"Result of (Condition 1 or Condition 2): {result1}")
    print("\n--- Test Case 2: True or True ---")
    result2 = condition1 or True
    print(f"Condition 1: {condition1}, True: True")
    print(f"Result of (Condition 1 or True): {result2}")
    print("\n--- Test Case 3: False or False ---")
    result3 = condition2 or condition3
    print(f"Condition 2: {condition2}, Condition 3: {condition3}")
    print(f"Result of (Condition 2 or Condition 3): {result3}")
    print("\n--- Test Case 4: False or True ---")
    result4 = condition3 or True
    print(f"Condition 3: {condition3}, True: True")
    print(f"Result of (Condition 3 or True): {result4}")
if __name__ == '__main__':
    main()