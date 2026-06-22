if __name__ == '__main__':
    pattern_length = 20
    repeat_pattern = 'AB'
    
    generated_pattern = ''.join([repeat_pattern for _ in range((pattern_length + 1) // len(repeat_pattern))])[:pattern_length]
    print(generated_pattern)