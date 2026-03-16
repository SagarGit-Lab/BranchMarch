def login(username, password):
    # Simple login function
    if username == "admin" and password == "admin123":
        return "Login successful!"
    else:
        return "Login failed! Please check your username and password."