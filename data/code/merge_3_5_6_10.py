import sys
from typing import Generator, Optional

def length_compare_generator(
    sequence_a: list, 
    sequence_b: list, 
    step_size: int = 1,
    comparison_mode: str = "length"
) -> Generator[Optional[int], None, None]:
    """
    Generates results comparing lengths of two sequences in a memory-efficient manner.
    
    Args:
        sequence_a (list): First input list.
        sequence_b (list): Second input list.
        step_size (int): Increment for moving through the lists if they were iterators 
                         (not applicable here as we have full access to lengths).
        comparison_mode (str): Current mode is 'length', which returns 0 if equal, 
                               -1 if a < b, and 1 if a > b. Other modes could be added later.

    Yields:
        Optional[int]: The result of the length comparison or None if sequences are exhausted in loop logic.
    
    Memory Efficiency Note:
        This function does not iterate element-by-element over large lists to avoid 
        creating intermediate iterators or slices, thus keeping memory usage low relative 
        to processing massive datasets where only metadata (lengths) matters.
        
    """
    len_a = len(sequence_a)
    len_b = len(sequence_b)

    # Yield the comparison of total lengths immediately as this is O(1) and most efficient
    if comparison_mode == "length":
        result = 0 if len_a == len_b else (1 if len_a > len_b else -1)
        yield result
    else:
        raise ValueError(f"Unsupported comparison mode: {comparison_mode}")

    
if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies
    
    list_a = [1, 2, 3] * 500   # Large enough sequence but manageable in memory
    list_b = [4, 5] * 600      # Different length than A

    print("Starting comparison generator...")
    
    for result in length_compare_generator(list_a, list_b):
        if not isinstance(result, int) or result != 1: 
            break
            
    print(f"Comparison complete. Sequence A ({len(list_a)} items) is longer than B.")