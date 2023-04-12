contact_book = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact found", ()
        except ValueError:
            return "Invalid input. Please try again", ()
        except IndexError:
            return "Invalid input. Please try again", ()
        except TypeError:
            return "Not enough params."
    return inner


@input_error
def add_contact(name, phone):
    contact_book[name] = phone
    return f"Contact {name} has been added with phone number {phone}"


@input_error
def change_contact(name, phone):
    contact_book[name] = phone
    return f"Phone number for contact {name} has been changed to {phone}"


@input_error
def get_phone_number(name):
    return f"The phone number for contact {name} is {contact_book[name]}"


def show_all_contacts(*args):
    if contact_book:
        return "\n".join([f"{name}: {phone}" for name, phone in contact_book.items()])
    else:
        return "There are no contacts saved in the book"


def hello(*args):
    return "How can I help you?"


def good_bye(*args):
    return "Good bye"


def no_command(*args):
    return "Invalid command. Please try again"


def parser(user_input):
    if user_input == "hello":
        return hello, ()

    elif user_input.startswith("add "):
        # try:
        data = user_input.replace("add", '').strip().split(" ")
        # except IndexError:
        #     return "Invalid input. Please try again"
        return add_contact, data

    elif user_input.startswith("change "):
        # try:
        data = user_input.replace("change", '').strip().split(" ")
        # except IndexError:
            # return "Invalid input. Please try again"
        return change_contact, data

    elif user_input.startswith("phone "):
        # try:
        data = user_input.replace("phone", '').strip().split(" ")
        # except IndexError:
        return get_phone_number, data

    elif user_input == "show all":
        return show_all_contacts, ()

    elif user_input in ["good bye", "close", "exit"]:
        return good_bye, ()
    
    else:
        return no_command, ()


def main():
    while True:
        user_input = input("Enter command: ").lower()
        command, data = parser(user_input)
        
        print(command(*data))
        
        if command == good_bye:
            break

      
if __name__ == "__main__":
    main()