def get_voter_eligibility(voter_attributes: dict) -> str:
    try:
        age = voter_attributes.get("age")
        citizenship = voter_attributes.get("citizenship")
        
        if age is None or citizenship is None:
            raise ValueError("Missing required attributes: age and citizenship")
        
        if not isinstance(age, (int, float)):
            raise TypeError("Age must be a number")
            
        if not isinstance(citizenship, str):
            raise TypeError("Citizenship must be a string")
            
        if age < 18:
            return "Underage"
            
        if citizenship.lower() != "citizen":
            return "Non-citizen"
            
        return "Eligible"
        
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    sample_voter = {"age": 25, "citizenship": "Citizen"}
    result = get_voter_eligibility(sample_voter)
    print(result)