import timeit

class ComparisonTool:
    """A utility class optimized for efficient numerical comparison."""

    def check_greater(self, value1, value2):
        """
        Compares two values and returns True if the first is strictly greater than the second.

        Optimizes by using Python's native integer handling which handles arbitrarily large numbers efficiently.
        For floats, uses standard comparison logic but avoids object creation overhead where possible via direct ops.

        Parameters:
            value1 (int or float): The first value to compare.
            value2 (int or float): The second value to compare.

        Returns:
            bool: True if value1 > value2, False otherwise.
        """
        # Direct comparison leverages C-level optimizations in Python for both int and float types.
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()

    # Sample large integer comparisons
    huge_num_1 = 456789012345678901234567890123456789
    huge_num_2 = 456789012345678901234567890123456788

    # Sample float comparisons (including large floats if needed, though int is primary target for "large number" context)
    large_float_1 = 1.2e308
    large_float_2 = 1.1e308

    print(f"{huge_num_1} > {huge_num_2}: {tool.check_greater(huge_num_1, huge_num_2)}")
    print(f"{large_float_1} > {large_float_2}: {tool.check_greater(large_float_1, large_float_2)}")

    # Performance benchmark simulation (local scope only)
    time_int = timeit.timeit('t.check_greater(9**100 - 5, 9**100)', setup='import sys; t=ComparisonTool()', number=10000)
    print(f"Time taken for 10k large int comparisons: {time_int:.4f} seconds")