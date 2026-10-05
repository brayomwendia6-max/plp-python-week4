def double(number):
    # Return the result of multiplying number by 2
    return number * 2
print(double(7))
print(double(10))
    
def is_pass(score):
    # Return the result of comparing score to 50
    return score >= 50
print(is_pass(60))
print(is_pass(40))

def greet(name, greeting="Hello"):
    # Return the greeting, a comma, the name, and an exclamation mark
    return f"{greeting}, {name}!"
print(greet("Amina"))
print(greet("Brian", "Habari"))