reverse_string = lambda s: ''.join(reversed(s))

if __name__ == '__main__':
    sample_text = "Alibaba Cloud"
    reversed_text = reverse_string(sample_text)
    print(f"Original: {sample_text}, Reversed: {reversed_text}")