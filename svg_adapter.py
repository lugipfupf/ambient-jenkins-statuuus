import time

import svgwrite


class SvgAdapter(object):
    radius = 10
    spacing = 1

    def __init__(self):
        pass

    def fade_to_colors(self, colors):
        offset = 0
        center_y = self.radius + self.spacing
        dwg = svgwrite.Drawing('status.svg')

        for i, color in enumerate(colors):
            center_x = self.spacing + self.radius + offset
            dwg.add(
                dwg.circle((center_x, center_y), self.radius, fill=svgwrite.rgb(color[0], color[1], color[2], 'RGB')))
            offset += 2 * self.radius + self.spacing

        dwg.save()

        time.sleep(3)
