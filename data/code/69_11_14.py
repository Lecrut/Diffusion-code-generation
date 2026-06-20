class StringIndexer:
    @staticmethod
    def print_selected_chars(s, indices):
        result = []
        for index in indices:
            if 0 <= index < len(s):
                result.append(s[index])
        return ''.join(result)

if __name__ == '__main__':
    sample_string = "HelloWorld"
    sample_indices = [0, 4, 7, 10]
    selected_chars = StringIndexer.print_selected_chars(sample_string, sample_indices)
    print(f"String: {sample_string}")
    print(f"Indices: {sample_indices}")
    print(f"Selected Characters: {selected_chars}")