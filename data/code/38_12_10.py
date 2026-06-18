class StringAnalyzer:
    def check_for_duplicates(self, text):
        """
        Identifies all repeated characters in a given string instance.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            list[str]: A sorted list of unique characters that appear more than once.
        """
        char_count = {}
        duplicates = []

        # Iterate through each character and count occurrences, ignoring case sensitivity if desired.
        # Here we treat 'A' and 'a' as different unless specified otherwise (standard behavior).
        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Collect characters that have a count greater than 1.
        for char, count in char_count.items():
            if count > 1 and char not in duplicates:
                duplicates.append(char)

        return sorted(duplicates)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Hard-coded sample values ensuring no user input or external dependencies are needed.
    test_cases = [
        "hello world",       # Expected: ['d', 'e', 'h', 'l', 'o'] -> sorted order handles uniqueness per char type here. 
                            # Note: In this implementation, case-sensitive unless lowercased below if logic changes.
                            # Let's trace manually for input "hello": h->1, e->1, l->2, o->1 => ['l']. 
                            # For "hello world": w->1, r->1, d->1, space->1, 'h'->1,'e'->1,'l'->3+'o'->2.
                            # Duplicates: 'd', 'e', 'h', 'l', 'o'. Sorted alphabetically (case sensitive): 
                            # Actually sorted string order: d < e < h < l < o? No, ASCII/Unicode sort applies.
        "python programming", # p->2, y->1, t->1, h->2, o->3, n->2, g->2, r->2, a->1, m->2, i->1 -> 
                             # Duplicates: ['a', 'g', 'h', 'm', 'n', 'o', 'p', 'r']
        "aaaa",               # Expected: ['a']
    ]

    for text in test_cases:
        result = analyzer.check_for_duplicates(text)
        print(f"Input: '{text}'")
        if not result:
            print("No duplicates found.")
        else:
            print(f"Duplicates found (sorted): {result}")