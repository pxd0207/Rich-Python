from typing import Dict

from .style import Style

DEFAULT_STYLES: Dict[str, Style] = {
    "none": Style("none"),
    "reset": Style.reset(),
    "dim": Style("dim", dim=True),
    "bright": Style("bright", dim=False),
    "bold": Style("bold", bold=True),
    "b": Style("bold", bold=True),
    "italic": Style("italic", italic=True),
    "i": Style("italic", italic=True),
    "underline": Style("underline", underline=True),
    "u": Style("underline", underline=True),
    "blink": Style("blink", blink=True),
    "blink2": Style("blink2", blink2=True),
    "reverse": Style("reverse", reverse=True),
    "strike": Style("strike", strike=True),
    "s": Style("strike", strike=True),
    "black": Style("black", color="black"),
    "red": Style("red", color="red"),
    "green": Style("green", color="green"),
    "yellow": Style("yellow", color="yellow"),
    "magenta": Style("magenta", color="magenta"),
    "cyan": Style("cyan", color="cyan"),
    "white": Style("white", color="white"),
    "on_black": Style("on_black", back="black"),
    "on_red": Style("on_red", back="red"),
    "on_green": Style("on_green", back="green"),
    "on_yellow": Style("on_yellow", back="yellow"),
    "on_magenta": Style("on_magenta", back="magenta"),
    "on_cyan": Style("on_cyan", back="cyan"),
    "on_white": Style("on_white", back="white"),
}

MARKDOWN_STYLES = {
    "markdown.paragraph": Style("markdown.paragraph"),
    "markdown.text": Style("markdown.text"),
    "markdown.emph": Style("markdown.emph", italic=True),
    "markdown.strong": Style("markdown.strong", bold=True),
    "markdown.code": Style("markdown.code", dim=True, bold=True),
    "markdown.code_block": Style(
        "markdown.code_block", dim=True, color="cyan", back="black"
    ),
    "markdown.block_quote": Style("markdown.code_block", color="magenta"),
    "markdown.list": Style("markdown.list", color="cyan"),
    "markdown.item": Style("markdown.item"),
    "markdown.item.bullet": Style("markdown.item", color="yellow", bold=True),
    "markdown.item.number": Style("markdown.item", color="yellow", bold=True),
    "markdown.hr": Style("markdown.hr", dim=True),
    "markdown.h1.border": Style("markdown.h1.border"),
    "markdown.h1": Style("markdown.h1", bold=True),
    "markdown.h2": Style("markdown.h2", bold=True, underline=True),
    "markdown.h3": Style("markdown.h3", bold=True),
    "markdown.h4": Style("markdown.h4", bold=True, dim=True),
    "markdown.h5": Style("margit kdown.h5", underline=True),
    "markdown.h6": Style("markdown.h6", italic=True),
    "markdown.h7": Style("markdown.h7", italic=True, dim=True),
    "markdown.link": Style(bold=True),
    "markdown.link_url": Style(underline=True),
}
DEFAULT_STYLES.update(MARKDOWN_STYLES)