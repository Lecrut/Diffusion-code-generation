class StringCompressor:
    DEFAULT_SEPARATOR = ""

    @staticmethod
    def compress(s):
        if not s:
            return ""
        compressed_parts = []
        current_char = s[0]
        run_length = 1
        for i in range(1, len(s)):
            if s[i] == current_char:
                run_length += 1
            else:
                compressed_parts.append(current_char + str(run_length))
                current_char = s[i]
                run_length = 1
        compressed_parts.append(current_char + str(run_length))
        return StringCompressor.DEFAULT_SEPARATOR.join(compressed_parts)

if __name__ == '__main__':
    sample_text = 'cccccccccc'
    output = StringCompressor.compress(sample_text)
    print(output)