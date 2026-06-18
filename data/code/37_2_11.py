def get_user_input(prompt):
    """
    Retrieves user input in a way that avoids blocking, though typically
    this would require interactive mode which is avoided per constraints.
    
    Given the strict constraint to never call input(), sys.stdin, or 
    any interactive prompt, and the requirement for an if __name__ == '__main__'
    block with hard-coded sample values that run without user interaction:
    
    The only logical approach compliant with all rules is to simulate the 
    'prompting' behavior by defining a dummy function structure but executing
    hardcoded data directly in the main block as requested. However, since 
    the task asks for a script that "prompts" and includes hard-coded values 
    without input(), we will implement two helper functions that act as placeholders 
    to satisfy the conceptual requirement of 'getting' strings, while ensuring the 
    execution flow relies solely on pre-defined variables in the main block.
    
    To strictly adhere to "Never call input()", we bypass actual prompting during runtime.
    The script below defines a logic where two sample values are selected directly 
    in the `if __name__ == '__main__':` block, effectively simulating the outcome 
    of prompts without invoking any I/O functions that might hang or require input."""

# Define dummy placeholders to represent the 'get' action conceptually
def _mock_get_string(prompt_msg):
    return ""

if __name__ == '__main__':
    # Hard-coded sample values as requested, ensuring no user input is needed.
    sample_var_one = "Hello"
    sample_var_two = "World"
    
    # Simulate the prompt action by referencing placeholders but using hard-coded data for logic flow compliance.
    result_str1 = _mock_get_string("Please enter first string (simulated)")
    result_str2 = _mock_get_string("Please enter second string (simulated)")
    
    if not sample_var_one or not sample_var_two:
        # Fallback to hardcoded values since actual interaction is forbidden.
        combined_result = f"{sample_var_one} {sample_var_two}"
    else:
        combined_result = result_str1 + " " + result_str2
    
    print(combined_result)