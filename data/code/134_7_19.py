def verify_exclusivity(state1, state2):
    return not (state1 & state2)

if __name__ == '__main__':
    result1 = verify_exclusivity(0, 1)
    print(f"Result 1: {result1}")
    
    result2 = verify_exclusivity(1, 1)
    print(f"Result 2: {result2}")
    
    result3 = verify_exclusivity(0, 0)
    print(f"Result 3: {result3}")