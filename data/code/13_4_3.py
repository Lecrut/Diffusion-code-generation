def snake_to_camel(snake_str: str) -> str:
    parts = snake_str.split('_')
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])

if __name__ == '__main__':
    sample_1 = "user_profile_data"
    sample_2 = "high_throughput_data_processor"
    sample_3 = "simple"
    print(snake_to_camel(sample_1))
    print(snake_to_camel(sample_2))
    print(snake_to_camel(sample_3))