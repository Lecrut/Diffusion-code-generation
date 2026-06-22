def determine_the_largest_number_present_summary():
    sample_data = [
        (10, 5, 22, 8),
        (3.14, 1.618, 2.718),
        ("apple", "banana", 100, "orange")
    ]
    
    for data in sample_data:
        numbers = [item for item in data if isinstance(item, (int, float))]
        largest_number = max(numbers) if numbers else None
        print(f"Input: {data}, Largest: {largest_number}")

if __name__ == '__main__':
    determine_the_largest_number_present_summary()