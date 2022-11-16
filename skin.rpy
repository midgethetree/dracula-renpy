init -2 python:

    # The color of non-interactive text.
    custom_text = "#f8f8f2"

    # Colors for buttons in various states.
    custom_idle = "#f8f8f2"
    custom_hover = "#bd93f9"
    custom_disable = "#f8f8f27f"

    # Colors for reversed text buttons (selected list entries).
    custom_reverse_idle = "#bd93f9"
    reverse_hover = "#8be9fd"
    custom_reverse_text = "#282a36"

    # Colors for the scrollbar thumb.
    custom_scrollbar_idle = "#dfdfdf"
    custom_scrollbar_hover = "#d86b45"

    # An image used as a separator pattern.
    custom_pattern = "images/pattern.png"

    # A displayable used for the background of everything.
    custom_background = "#1e1f29"

    # A displayable used for the background of the projects list.
    custom_projects_window = "#282a36"

    # A displayable used the background of information boxes.
    custom_info_window = "#282a36"

    # Colors for the titles of information boxes.
    custom_error_color = "#ff5555"
    custom_info_color = "#f3f3f3"
    custom_interaction_color = "#bd939f"
    custom_question_color = "#8be9fd"

    # The color of input text.
    custom_input_color = "#bd939f"

    # A displayable used for the background of windows
    # containing commands, preferences, and navigation info.

    custom_window = Frame(Fixed(Solid(custom_reverse_idle, xsize=4, xalign=0), Solid(custom_info_window, xsize=794, xalign=1.0), xsize=800, ysize=600), 0, 0, tile=True)
