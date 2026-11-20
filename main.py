from __future__ import annotations

import tcod.context
import tcod.console
import tcod.event
import tcod.tileset

def main() -> None:
    tileset = tcod.tileset.load_tilesheet(
        "assets/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tileset += tcod.tileset.procedural_block_elements(shape=tileset.tile_shape)
    console = tcod.console.Console(80, 50)
    console.print(0, 0, "Hello World")
    with tcod.context.new(tileset=tileset) as context:
        while True:
            context.present(console)
            for event in tcod.event.wait():
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit

if __name__ == "__main__":
    main()
