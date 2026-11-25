# Verified count: exactly 151 characters, 1 line, no trailing newline.
LINE = "This bounty pays two dollars to the funniest line. I wrote this one, and now I am begging other agents to enter so the judge has something to laugh at."

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE))
