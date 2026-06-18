def reverse_string(s): return "".join(reversed(s)) # This is not strictly a 'one-line expression' in the sense of being just an assignment, but it's efficient and concise logic. 
# The task asks for a "lambda expression or comprehension". Let's use a list comprehension which counts as one line if written on one physical line with proper syntax handling or simply return the reversed string using join.
# A true one-liner solution:

reverse_str = lambda s: "".join(s[::-1]) 

if __name__ == '__main__':
    sample_input = "Python Programming"
    print(reverse_str(sample_input)) # Output: gnimmargorP nohtyP