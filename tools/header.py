# Uso (desde la raíz del repo): python3 tools/header.py && python3 tools/header.py movil
# Genera assets/header.svg: portada animada (sin JavaScript: GitHub la muestra como imagen).
import sys
MOBILE = len(sys.argv) > 1 and sys.argv[1] == 'movil'
W, H = (480, 612) if MOBILE else (900, 340)
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
TX, TY, TW, TH = (24, 320, 432, 268) if MOBILE else (478, 36, 392, 268)      # ventana de terminal
CHAR = 7.9                               # ancho aprox. de un carácter a 13px
P = '<tspan fill="#3fb950">❯</tspan> '

# (texto con tspans, nº de caracteres visibles, es comando)
lines = [
  (P + 'whoami', 8, True),
  ('<tspan fill="#e6edf3">Luis Rafael</tspan> <tspan fill="#8b949e">· dev full-stack</tspan>', 28, False),
  (P + 'cat stack.txt', 15, True),
  ('<tspan fill="#79c0ff">TypeScript</tspan> <tspan fill="#61dafb">React</tspan> <tspan fill="#8cc84b">Node</tspan> '
   '<tspan fill="#ffd43b">Python</tspan> <tspan fill="#c4b5fd">Solidity</tspan>', 37, False),
  (P + 'ls ~/proyectos', 16, True),
  ('<tspan fill="#ffa657">macmovil.com</tspan>  <tspan fill="#d2a8ff">web3-game</tspan>  <tspan fill="#7ee787">crypto-sentinel</tspan>', 41, False),
  ('<tspan fill="#a5d6ff">notarizacion</tspan>  <tspan fill="#ff7b72">dolar-acurast</tspan>', 27, False),
]

t = 0.6
clips, texts = [], []
for i, (body, n, cmd) in enumerate(lines):
    y = TY + 62 + i * 25
    dur = n * 0.075 if cmd else 0.12
    full = 18 + n * CHAR + 30
    clips.append(f'<clipPath id="l{i}"><rect x="{TX+16}" y="{y-16}" height="24" width="0">'
                 f'<animate attributeName="width" from="0" to="{full:.0f}" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze"'
                 f'{" calcMode=\"discrete\" values=\"0;" + format(full, ".0f") + "\" keyTimes=\"0;0.01\"" if not cmd else ""}/></rect></clipPath>')
    indent = 0 if cmd else 16
    texts.append(f'<text x="{TX+18+indent}" y="{y}" clip-path="url(#l{i})">{body}</text>')
    t += dur + (0.35 if cmd else 0.18)

cursor_y = TY + 62 + len(lines) * 25
cursor_begin = t

chips = ['E-commerce', 'Smart contracts', 'Bots de Telegram', 'IA local']
chip_svg, cx, cy = [], 40, 240
for k, label in enumerate(chips):
    w = len(label) * 7.6 + 26
    if cx + w > (W - 30 if MOBILE else 440):  # segunda fila
        cx, cy = 40, cy + 36
    chip_svg.append(
        f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{0.9 + k*0.25:.2f}s" dur="0.5s" fill="freeze"/>'
        f'<rect x="{cx:.0f}" y="{cy}" width="{w:.0f}" height="28" rx="14" fill="#ffffff" fill-opacity="0.06" stroke="#ffffff" stroke-opacity="0.14"/>'
        f'<text x="{cx + w/2:.0f}" y="{cy+19}" text-anchor="middle" font-size="12.5" fill="#c9d1d9">{label}</text></g>')
    cx += w + 8

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">Luis Rafael Corales — @ioskpu</title>
<desc id="d">Desarrollador full-stack en Colombia: e-commerce, smart contracts, bots de Telegram e IA local. Stack: TypeScript, React, Node, Python y Solidity.</desc>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b0f19"/><stop offset="1" stop-color="#161233"/></linearGradient>
  <radialGradient id="o1"><stop offset="0" stop-color="#7c3aed" stop-opacity=".55"/><stop offset="1" stop-color="#7c3aed" stop-opacity="0"/></radialGradient>
  <radialGradient id="o2"><stop offset="0" stop-color="#0ea5e9" stop-opacity=".45"/><stop offset="1" stop-color="#0ea5e9" stop-opacity="0"/></radialGradient>
  <radialGradient id="o3"><stop offset="0" stop-color="#f97316" stop-opacity=".35"/><stop offset="1" stop-color="#f97316" stop-opacity="0"/></radialGradient>
  <linearGradient id="name" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="440" y2="0" spreadMethod="reflect">
    <stop offset="0" stop-color="#a78bfa"/><stop offset=".5" stop-color="#38bdf8"/><stop offset="1" stop-color="#fb923c"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-160 0;160 0;-160 0" dur="9s" repeatCount="indefinite"/>
  </linearGradient>
  <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#ffffff" stroke-opacity=".045"/></pattern>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  {''.join(clips)}
</defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <circle cx="160" cy="40" r="220" fill="url(#o1)"><animate attributeName="cx" values="160;260;160" dur="14s" repeatCount="indefinite"/></circle>
  <circle cx="760" cy="320" r="240" fill="url(#o2)"><animate attributeName="cy" values="320;250;320" dur="11s" repeatCount="indefinite"/></circle>
  <circle cx="460" cy="380" r="170" fill="url(#o3)"><animate attributeName="cx" values="460;380;460" dur="16s" repeatCount="indefinite"/></circle>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="#ffffff" stroke-opacity=".08"/>

<g font-family="{SANS}">
  <text x="40" y="78" font-size="15" fill="#8b949e" letter-spacing="2">HOLA, SOY</text>
  <text x="40" y="124" font-size="38" font-weight="700" fill="url(#name)">Luis Rafael</text>
  <text x="40" y="166" font-size="38" font-weight="700" fill="url(#name)">Corales</text>
  <text x="40" y="200" font-size="16" fill="#c9d1d9">Construyo tiendas en línea, bots y contratos</text>
  <text x="40" y="222" font-size="16" fill="#c9d1d9">inteligentes desde <tspan fill="#ffd43b">Col</tspan><tspan fill="#58a6ff">om</tspan><tspan fill="#ff7b72">bia</tspan>.</text>
  {''.join(chip_svg)}
</g>

<g>
  <rect x="{TX}" y="{TY}" width="{TW}" height="{TH}" rx="12" fill="#0d1117" fill-opacity=".92" stroke="#30363d"/>
  <path d="M{TX} {TY+12}a12 12 0 0 1 12-12h{TW-24}a12 12 0 0 1 12 12v18H{TX}z" fill="#161b22"/>
  <circle cx="{TX+20}" cy="{TY+15}" r="5.5" fill="#ff5f57"/><circle cx="{TX+38}" cy="{TY+15}" r="5.5" fill="#febc2e"/><circle cx="{TX+56}" cy="{TY+15}" r="5.5" fill="#28c840"/>
  <text x="{TX+TW/2}" y="{TY+19}" text-anchor="middle" font-family="{MONO}" font-size="11.5" fill="#8b949e">~/ioskpu — zsh</text>
  <g font-family="{MONO}" font-size="13" fill="#c9d1d9" xml:space="preserve">
    {''.join(texts)}
    <text x="{TX+18}" y="{cursor_y}" opacity="0"><tspan fill="#3fb950">❯</tspan>
      <animate attributeName="opacity" to="1" begin="{cursor_begin:.2f}s" dur="0.01s" fill="freeze"/></text>
    <rect x="{TX+36}" y="{cursor_y-12}" width="8" height="15" fill="#c9d1d9" opacity="0">
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.01;0.5;0.51" dur="1.1s" begin="{cursor_begin:.2f}s" repeatCount="indefinite"/>
    </rect>
  </g>
</g>
</svg>
'''
open('assets/' + ('header-movil.svg' if MOBILE else 'header.svg'), 'w').write(svg)
print(len(svg), 'bytes; cursor at', round(cursor_begin, 2), 's')
