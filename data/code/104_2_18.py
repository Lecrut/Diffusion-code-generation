def compare_timestamps(timestamp1, timestamp2):
    if not isinstance(timestamp1, int) or not isinstance(timestamp2, int):
        raise ValueError("Both timestamps must be integers.")
    
    return abs(timestamp1 - timestamp2)

if __name__ == '__main__':
    result = compare_timestamps(1673980800, 1674067200)
    print(f"Difference in seconds: {result}")