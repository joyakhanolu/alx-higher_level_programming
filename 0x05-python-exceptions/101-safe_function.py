#!/usr/bin/python3
def safe_function(fct, *args):
    """
    Executes a function safely

    Args:
        fct: pointer to a function
        args: arguments passed to function

    Return:
        Result of the function otherwise, None
    """
    from sys import stderr
    try:
        return fct(*args)
    except ZeroDivisionError as err:
        print('Exception: {}'.format(err), file=stderr)
    except ValueError as va:
        print('Exception: {}'.format(va), file=stderr)
    except TypeError as tp:
        print('Exception: {}'.format(tp), file=stderr)
    except IndexError as ind:
        print('Exception: {}'.format(ind), file=stderr)
