class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        """
        Efficiently build a string from a list of parts using the built-in str.join().
        
        Args:
            parts (list[str]): The list of strings to concatenate.
            separator (str): The string to use as the delimiter between elements. Default is ' '.
            fill_value (str): If empty, used when an element in the list itself represents a missing value 
                             or None, though standard join does not handle internal replacements automatically.
                               This parameter acts here only if parts contains placeholders like '__MISSING__',
                               but since Python's str.join cannot do conditional replacement on-the-fly without logic,
                               we assume 'fill_value' might be intended for post-processing or specific placeholder handling.
                               
        However, strictly adhering to the task of utilizing `str.join()` efficiently: 
        If parts contains a special marker (like '__MISSING__'), it would require manual substitution before joining
        which violates pure join efficiency unless we pre-process. Given the constraint "utilizing built-in str.join()",
        and no explicit instruction on how fill_value interacts with content, 
        this implementation assumes 'fill_value' is for elements that might be None or empty if not handled by user,
        OR it serves as a default only if parts contains non-string objects (unlikely given type hint).
        
        The most direct interpretation for "optimized method... utilizing str.join":
        Simply return separator-joined string. 
        If fill_value is intended to replace specific items in 'parts', that requires iteration, not pure join efficiency.
        But the prompt says: "fill_value" argument exists. Let's assume it replaces empty strings or None if passed?
        
        Actually, re-reading: "efficiently build a string... utilizing str.join". 
        The fill_value is likely meant to replace specific missing indicators in parts before joining, but without explicit rules (e.g., which item gets replaced),
        we cannot invent logic. 
        
        Correction based on common patterns: Often such tasks imply replacing None or empty strings with fill_value if they appear?
        But the prompt doesn't say "replace empty/None". It just lists arguments. 
        To be safe and strictly efficient using join, I will process parts first to remove placeholders IF any logic is implied by context of 'fill_value',
        but since none is defined, I'll assume fill_value does nothing unless we see a pattern like '__MISSING__'.
        
        Wait, looking at similar problems: Usually `fill_value` implies replacing something. Without specification, 
        the most robust optimized join is just joining parts with separator. 
        However, if 'parts' might contain None and user expects fill_value to act there? No type hint says list[str].
        
        Let's implement it as simply joining, but adding a small pre-check: if any element in parts equals '__MISSING__' (common placeholder), replace with fill_value before join. 
        This adds minimal overhead for clarity while keeping 'join' the core engine. If no such marker exists, performance is O(n) from join itself.
        
        Optimization Note: Converting list to tuple or other structures doesn't help here; direct join on list[str] is already C-optimized in Python 3."""

        # Pre-process parts if we assume '__MISSING__' as a placeholder (common convention when fill_value exists without explicit rules)
        processed_parts = []
        for part in parts:
            if isinstance(part, str) and part == '__MISSING__':
                processed_parts.append(fill_value)
            else:
                # Ensure non-string elements are handled gracefully or ignored? 
                # Given type hint is list[str], we assume all are strings. If not string, skip to avoid crash in join if mixed types were passed accidentally?
                # But strict typing says str. We'll cast just in case for safety but rely on join's expectation of iterable of strings.
                processed_parts.append(part)

        return separator.join(processed_parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    sample_list = ['Hello', 'World']
    result1 = assembler.join_parts(sample_list, ', ')
    print(f"Joined with ', ': {result1}")

    # Test with fill_value placeholder logic assuming '__MISSING__' usage
    parts_with_missing = ['Good', '__MISSING__', 'Morning']
    result2 = assembler.join(parts_with_missing, sep='-', filler='')
    print(f"With missing replaced by empty: '{result2}'")
    
    # Standard case with fill_value having content
    parts_normal = ['A', 'B']
    res3 = assembler.join_parts(parts_normal)
    print(f"Default join: {res3}")