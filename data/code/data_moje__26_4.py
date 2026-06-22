def get_voting_status(age, threshold=18):
    is_voter = age >= threshold
    status = "eligible" if is_voter else "not eligible"
    return {"age": age, "threshold": threshold, "status": status}

if __name__ == '__main__':
    result = get_voting_status(20)
    print(result)
    result2 = get_voting_status(16)
    print(result2)