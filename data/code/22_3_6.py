if __name__ == '__main__':
    num = 17; expr = lambda n: n % 2 != 0; check_result = expr(num); print(f"The number {num} is odd" if check_result else f"{num} is even") # This is a multi-line block inside the single line statement above? No, I need to ensure it's all one logical expression or code block.
# Re-reading: "Write a concise, single-line Python expression... Provide an example using 17". 
# And "Return only a single complete runnable Python module." with `if __name__ == '__main__':` block.
# The expression itself doesn't have to be the entire script content if it's inside the main block? No, usually these prompts want the logic defined cleanly. Let's make the check happen in one line within the main execution flow as requested by "single-line Python expression".

num = 17; print("Odd" if num % 2 != 0 else "Even") # This is a single statement block effectively doing the work but technically two statements (assignment and call). 
# To make it strictly one line of code in the main block:
if __name__ == '__main__':
    num = 17; print("Odd" if num % 2 != 0 else "Even")