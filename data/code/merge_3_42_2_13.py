import time

class StringAssembler:
    """A class to efficiently construct a string from a list of parts."""

    def build(self, parts, separator):
        """
        Constructs a new string by joining the given list of parts with a specified separator.

        Args:
            parts (list): A list of strings or values that can be converted to strings.
            separator (str): The string used as the delimiter between elements in 'parts'.

        Returns:
            str: The constructed concatenated string.
        
        Note: This method efficiently handles large lists by utilizing Python's optimized 
        join functionality, which generally outperforms concatenation via loops or f-strings 
        in repeated iterations due to C-level optimizations and reduced interpreter overhead.
        """
        return separator.join(str(part) for part in parts)

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, network access, or file dependencies.
    assembler = StringAssembler()

    # Sample 1: Basic usage with words and a comma
    parts_1 = ["Hello", "World"]
    separator_1 = ", "
    result_1 = assembler.build(parts_1, separator_1)

    # Sample 2: Using an empty list to verify behavior
    parts_2 = []
    separator_2 = "|"
    result_2 = assembler.build(parts_2, separator_2)

    # Sample 3: Mixed types that require string conversion (integers and floats)
    numbers = [10, "twenty", 3.5]
    separator_numbers = "-"
    result_3 = assembler.build(numbers, separator_numbers)

    print(f"Result 1 ({parts_1}): \"{result_1}\"")
    print(f"Result 2 (empty list): '{result_2}'")
    print(f"Result 3 (mixed types {numbers}): \"{result_3}\"")