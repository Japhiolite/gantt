# label of packages
packages = (
    "WP 1-1", "WP 1-2",
    "WP 2-1", "WP 2-2", "WP 2-3", "WP 2-4",
    "WP 3-1", "WP 3-2", "WP 3-3",
)

timing = {
    "WP 1-1": "0, 2",
    "WP 1-2": "2, 4",
    "WP 2-1": "3, 5",
    "WP 2-2": "6, 8",
    "WP 2-3": "7, 9",
    "WP 2-4": "8, 9",
    "WP 3-1": "2, 6 ",
    "WP 3-2": "4, 8 ",
    "WP 3-3": "6, 12"
}

# miles stones are optional
milestones = {
    "WP 1-1": [2],
    "WP 1-2": [3, 4],
    "WP 2-1": [5],
    "WP 2-2": [8],
    "WP 2-3": [8],
    "WP 2-4": [9],
    "WP 3-1": [4,6],
    "WP 3-2": [8],
    "WP 3-3": [11.9] # 12 is not good to read
}

title = r" Sample GANTT for \textbf{myProject}"
xlabel = "time (weeks)"
xticks = [2,4,6,8,10,12]        #optional