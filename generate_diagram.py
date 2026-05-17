import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(18, 11))
ax.set_xlim(0, 18)
ax.set_ylim(0, 11)
ax.axis('off')
fig.patch.set_facecolor('#F8F9FA')

# Title
ax.text(9, 10.4, 'AI-Powered Medical Image Triage System', ha='center',
        fontsize=18, fontweight='bold', color='#2C3E50')
ax.text(9, 9.9, 'Solution Architecture', ha='center',
        fontsize=13, color='#7F8C8D')

# Main pipeline boxes - wider and more spaced
steps = [
    (0.3, 7.0, 2.8, 2.2, '1. Image Capture', '#E8F6F3', '#1ABC9C',
     'Medical scan\nX-Ray / CT / MRI'),
    (3.5, 7.0, 2.8, 2.2, '2. Data\nPreprocessing', '#EAF2FB', '#2980B9',
     'Resize\nNormalize\nEnhance Quality'),
    (6.7, 7.0, 2.8, 2.2, '3. AI Model\n(ResNet50 CNN)', '#FEF9E7', '#F39C12',
     'CNN extracts features\nand learns patterns\nfrom scan images'),
    (9.9, 7.0, 2.8, 2.2, '4. Diagnosis\nClassification', '#FDEDEC', '#E74C3C',
     'Normal\nPneumonia\nTumor / Fracture'),
    (13.1, 7.0, 2.8, 2.2, '5. Doctor Review\nDashboard', '#F4ECF7', '#8E44AD',
     'Real-time Results\nKPI Monitoring\nAlerts & Reports'),
]

for x, y, w, h, label, facecolor, edgecolor, subtext in steps:
    rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                          facecolor=facecolor, edgecolor=edgecolor, linewidth=2.5)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h - 0.5, label, ha='center', va='center',
            fontsize=10, fontweight='bold', color='#2C3E50')
    ax.text(x + w/2, y + 0.7, subtext, ha='center', va='center',
            fontsize=8, color='#555555')

# Arrows between main boxes
arrow_xs = [3.1, 6.3, 9.5, 12.7]
for x in arrow_xs:
    ax.annotate('', xy=(x + 0.35, 8.1), xytext=(x, 8.1),
                arrowprops=dict(arrowstyle='->', color='#2C3E50', lw=2.5))

# Vertical arrow down from AI Model box
ax.annotate('', xy=(8.1, 5.8), xytext=(8.1, 7.0),
            arrowprops=dict(arrowstyle='->', color='#2C3E50', lw=2.5))

# Decision diamond
dx, dy = 8.1, 4.8
diamond = plt.Polygon([
    [dx, dy + 0.9],
    [dx + 1.4, dy],
    [dx, dy - 0.9],
    [dx - 1.4, dy]
], facecolor='#FDF2E9', edgecolor='#E67E22', linewidth=2.5)
ax.add_patch(diamond)
ax.text(dx, dy + 0.25, 'Critical', ha='center', va='center',
        fontsize=9, fontweight='bold', color='#E67E22')
ax.text(dx, dy - 0.25, 'Case?', ha='center', va='center',
        fontsize=9, fontweight='bold', color='#E67E22')

# YES arrow and box (right side)
ax.annotate('', xy=(12.0, 4.8), xytext=(9.5, 4.8),
            arrowprops=dict(arrowstyle='->', color='#E74C3C', lw=2.5))
ax.text(10.7, 5.1, 'YES', fontsize=9, color='#E74C3C', fontweight='bold')

urgent = FancyBboxPatch((12.0, 4.2), 3.0, 1.2, boxstyle="round,pad=0.15",
                         facecolor='#FDEDEC', edgecolor='#E74C3C', linewidth=2.5)
ax.add_patch(urgent)
ax.text(13.5, 4.9, 'Urgent Review', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#E74C3C')
ax.text(13.5, 4.5, 'Flag & Alert Doctor', ha='center', va='center',
        fontsize=9, color='#E74C3C')

# NO arrow and box (left side)
ax.annotate('', xy=(4.5, 4.8), xytext=(6.7, 4.8),
            arrowprops=dict(arrowstyle='->', color='#1ABC9C', lw=2.5))
ax.text(5.4, 5.1, 'NO', fontsize=9, color='#1ABC9C', fontweight='bold')

normal = FancyBboxPatch((1.5, 4.2), 3.0, 1.2, boxstyle="round,pad=0.15",
                         facecolor='#E8F8F5', edgecolor='#1ABC9C', linewidth=2.5)
ax.add_patch(normal)
ax.text(3.0, 4.9, 'Normal Queue', ha='center', va='center',
        fontsize=10, fontweight='bold', color='#1ABC9C')
ax.text(3.0, 4.5, 'Scheduled Review', ha='center', va='center',
        fontsize=9, color='#1ABC9C')

# Feedback loop box
feedback = FancyBboxPatch((0.5, 1.5), 17.0, 2.0, boxstyle="round,pad=0.15",
                           facecolor='#EBF5FB', edgecolor='#2980B9',
                           linewidth=2, linestyle='dashed')
ax.add_patch(feedback)
ax.text(9.0, 3.3, '6. Feedback Loop & Continuous Improvement',
        ha='center', fontsize=11, fontweight='bold', color='#2980B9')

# Feedback steps
fb_steps = [
    (2.5, 2.3, 'Collect\nNew Data'),
    (6.0, 2.3, 'Retrain &\nImprove Model'),
    (9.5, 2.3, 'Monitor\nPerformance'),
    (13.5, 2.3, 'Human Review\nfor Edge Cases'),
]
for x, y, txt in fb_steps:
    ax.text(x, y, txt, ha='center', va='center', fontsize=9, color='#2C3E50')

# Arrows in feedback loop
for x in [3.8, 7.5, 11.2]:
    ax.annotate('', xy=(x + 0.5, 2.5), xytext=(x, 2.5),
                arrowprops=dict(arrowstyle='->', color='#2980B9', lw=1.8))

# Legend
legend_items = [
    ('#1ABC9C', 'Data Acquisition'),
    ('#2980B9', 'Preprocessing'),
    ('#F39C12', 'AI Model'),
    ('#E74C3C', 'Prediction'),
    ('#8E44AD', 'Monitoring & Analytics'),
]
for i, (color, label) in enumerate(legend_items):
    ax.add_patch(mpatches.Rectangle((0.5 + i * 3.4, 0.5), 0.5, 0.3,
                                     facecolor=color, edgecolor='none'))
    ax.text(1.1 + i * 3.4, 0.65, label, fontsize=9, va='center', color='#2C3E50')

plt.tight_layout()
plt.savefig(r'C:\Users\SHIVANI\Desktop\Module5_Assignment\part-4-ai-solution-design\diagrams\solution_architecture.png',
            dpi=150, bbox_inches='tight', facecolor='#F8F9FA')
plt.show()
print("Diagram saved")