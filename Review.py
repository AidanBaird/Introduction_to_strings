# Define a function that generates a username consisting of the first three letters of the first and last name

def username_generator(first_name, last_name):
    username = first_name[0:3] + last_name[0:4]
    return username

username = username_generator("Abe", "Simpson")
print(username_generator("Abe", "Simpson"))
print(username)
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

print(password_generator(username))