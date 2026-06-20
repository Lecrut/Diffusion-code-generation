def get_opposite(boolean: bool) -> bool:
    return not boolean

if __name__ == '__main__':
    try:
        sample1 = True
        result1 = get_opposite(sample1)
        print(f"Input: {sample1}, Output: {result1}")
        
        sample2 = False
        result2 = get_opposite(sample2)
        print(f"Input: {sample2}, Output: {result2}")
    except Exception as e:
        print(f"Error: {e}")