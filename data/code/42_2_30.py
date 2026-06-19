class StringAssembler:

    def build(self, parts, separator):
        result = ''
        for part in parts:
            if result:
                result += separator
            result += part
        return result
if __name__ == '__main__':
    assembler = StringAssembler()
    sample_parts_1 = ['hello', 'world', 'python']
    sample_separator_1 = ' '
    output_1 = assembler.build(sample_parts_1, sample_separator_1)
    print(f'Output 1: {output_1}')
    sample_parts_2 = ['apple', 'banana', 'cherry', 'date']
    sample_separator_2 = '-'
    output_2 = assembler.build(sample_parts_2, sample_separator_2)
    print(f'Output 2: {output_2}')
    sample_parts_3 = ['one', 'two', 'three']
    sample_separator_3 = ', '
    output_3 = assembler.build(sample_parts_3, sample_separator_3)
    print(f'Output 3: {output_3}')