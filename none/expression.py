import random
from typing import Union, Sequence, Callable

from .message import escape

Expression_T = Union[str, Sequence[str], Callable]


def render(expr: Expression_T, *, escape_args=True,
           **kwargs) -> str:
    """
    Render an expression to message string.

    :param expr: expression to render
    :param escape_args: should escape arguments or not
    :param kwargs: keyword arguments used in str.format()
    :return: the rendered message
    """
    if isinstance(expr, Callable):
        expr = expr(**kwargs)
    elif isinstance(expr, Sequence) and not isinstance(expr, str):
        expr = random.choice(expr)
    if escape_args:
        for k, v in kwargs.items():
            if isinstance(v, str):
                kwargs[k] = escape(v)
    return expr.format(**kwargs)
