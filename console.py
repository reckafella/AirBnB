#!/usr/bin/env python3

"""
Module contains class implementing a simple command line interpreter
"""
import cmd, os, readline

class Console(cmd.Cmd):
    """ class implementing a simple command line interpreter """
    if os.getuid() == 0:
        prompt = "# "
    else:
        prompt = "$ "

    intro = '\n'.join(['\tWelcome to shell.',
                       '\tType `help` or `?` to list commands'])

    def do_greet(self, person):
        """
        Print 'Hello [person]!' when user types 'greet [person]'

        Else: Print 'Hello!' when user types 'greet'

        Args:
            person (str): a person's name
        """
        if person:
            print("Hello {}!".format(person.capitalize()))
        else:
            print("Hello!")

    def do_EOF(self, line):
        """
        Exit shell by typing 'EOF' or Pressing 'Ctrl+D'
        """
        return True

    def postloop(self):
        """ Method called after exiting loop """
        print()

    def do_exit(self, line):
        """ Exit the command prompt shell when user types 'exit'. """
        #print("{}".format(self.lastcmd))
        return True

    def do_clear(self, line):
        """ clear console """
        os.system('clear')

    def do_history(self, line):
        """ list run commands """
        for i in range(readline.get_current_history_length()):
            print(readline.get_history_item(i + 1))

    def help_greet(self):
        """ Help for greet command """
        print("Print 'Hello [person]!' when user types 'greet [person]'")
        print("\nElse:\n\tPrint 'Hello!' when user types 'greet'")

    def help_exit(self):
        """ Help for exit command """
        print(
            '\n'.join(
                ["Exit the command prompt shell when user types 'exit'."]
            )
        )

    def help_EOF(self):
        """ Help for EOF command """
        print(
            '\n'.join(["Exit shell by typing 'EOF' or Pressing 'Ctrl+D'"])
        )


if __name__ == "__main__":
    Console().cmdloop()
