# Dictionary to store username-password pairs, update this with our passwords and usernames. 
credentials = {
    '120': 'abc',
    '121': 'def',
    '122': 'ghi',
    '123': 'jkl'
}

# Get input from the user
username_input = input("Enter your username: ")

# Check if username is correct
if username_input in credentials:
    print('username registered')
else:
    print('username not registered')
    end

password_input=input('Enter your password:')

# Check if password is correct
if credentials[username_input] == password_input:
    print("Login successful!")
else:
    print("Invalid password.")
