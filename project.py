def find_substrings(s):
    substrings = []
    length = len(s)
    
    # Generate all possible substrings
    for start in range(length):
        for end in range(start + 1, length + 1):
            substrings.append(s[start:end])
    
    return substrings

# Example usage
input_string = "abc"
result = find_substrings(input_string)
print("Substrings of '{}':".format(input_string))
print(result)
